# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is the AST rewriter, it sits between the Parser and the Logical Planner.

~~~
                      ┌───────────┐
                      │   USER    │
         ┌────────────┤           ◄────────────┐
         │SQL         └───────────┘            │
  ───────┼─────────────────────────────────────┼──────
         │                                     │
   ┌─────▼─────┐                               │
   │ SQL       │                               │
   │  Rewriter │                               │
   └─────┬─────┘                               │
         │SQL                                  │Plan
   ┌─────▼─────┐                         ┌─────┴─────┐
   │           │                         │           │
   │ Parser    │                         │ Executor  │
   └─────┬─────┘                         └─────▲─────┘
         │AST                                  │Plan
   ╔═════▼═════╗      ┌───────────┐      ┌─────┴─────┐
   ║ AST       ║      │           │Stats │Cost-Based │
   ║ Rewriter  ║      │ Catalogue ├──────► Optimizer │
   ╚═════╦═════╝      └─────┬─────┘      └─────▲─────┘
         │AST               │Schemas           │Plan
   ┌─────▼─────┐      ┌─────▼─────┐      ┌─────┴─────┐
   │ Logical   │ Plan │           │ Plan │ Heuristic │
   │   Planner ├──────► Binder    ├──────► Optimizer │
   └───────────┘      └───────────┘      └───────────┘
~~~

It's primary role is to bind information to the AST which is provided in the order they appear
in the AST. For example, parameter substitutions and temporal ranges. Both of these require the
AST to be in the same order as the SQL provided by the user, which we can't guarantee after the
logical planner.

The parameter substitution is done after the AST is parsed to limit the possibility of the values
in the parameters affecting how the SQL is parsed (i.e. to prevent injection attacks). For similar
reasons, we do variable subsitutions here aswell. Although these are not sensitive to ordering, 
we should remove any opportunity for them to be used for injection attacks so we bind them after
the building of the AST.

The temporal range binding is done here because it is a non-standard extention not supported by
the AST parser, so we strip the temporal ranges out in the SQL rewriter, and add them to the AST
here.
"""
import datetime
import decimal

import numpy
from orso.tools import random_string

from opteryx.exceptions import ParameterError


def _build_literal_node(value):
    """for a given literal, write the AST node for it"""
    if value is None:
        return {"Value": "Null"}
    if isinstance(value, (bool)):
        # boolean must be before numeric
        return {"Value": {"Boolean": value}}
    if isinstance(value, (str)):
        return {"Value": {"SingleQuotedString": value}}
    if isinstance(value, (int, float, decimal.Decimal)):
        return {"Value": {"Number": [value, False]}}
    if isinstance(value, (numpy.datetime64)):
        return {"Value": {"SingleQuotedString": value.item().isoformat()}}
    if isinstance(value, (datetime.date, datetime.datetime, datetime.time)):
        return {"Value": {"SingleQuotedString": value.isoformat()}}


def parameter_binder(node, parameter_set, connection, query_type):
    """Walk the AST replacing 'Placeholder' nodes, this is recursive"""
    # Replace placeholders with parameters.
    # We do this after the AST has been parsed to remove any chance of the parameter affecting the
    # meaning of any of the other tokens - i.e. to eliminate this feature being used for SQL
    # injection.
    if isinstance(node, list):
        return [parameter_binder(i, parameter_set, connection, query_type) for i in node]
    if isinstance(node, dict):
        if "Value" in node:
            if "Placeholder" in node["Value"]:
                # fmt:off
                if len(parameter_set) == 0:
                    raise ParameterError("Incorrect number of bindings supplied."
                    " More placeholders are provided than parameters.")
                placeholder_value = parameter_set.pop(0)
                # prepared statements will have parsed this already
                if hasattr(placeholder_value, "value"):
                    placeholder_value = placeholder_value.value
                return _build_literal_node(placeholder_value)
                # fmt:on
        return {
            k: parameter_binder(v, parameter_set, connection, query_type) for k, v in node.items()
        }
    # we're a leaf
    return node


def temporal_range_binder(ast, filters):
    if isinstance(ast, (list)):
        return [temporal_range_binder(node, filters) for node in ast]
    if isinstance(ast, (dict)):
        node_name = next(iter(ast))
        if node_name == "Table":
            temporal_range = filters.pop(0)
            ast["Table"]["start_date"] = temporal_range[1]
            ast["Table"]["end_date"] = temporal_range[2]
            return ast
        if "table_name" in ast:
            temporal_range = filters.pop(0)
            ast["table_name"][0]["start_date"] = temporal_range[1]
            ast["table_name"][0]["end_date"] = temporal_range[2]
            return ast
        if "ShowCreate" in ast:
            temporal_range = filters.pop(0)
            ast["ShowCreate"]["start_date"] = temporal_range[1]
            ast["ShowCreate"]["end_date"] = temporal_range[2]
            return ast
        return {k: temporal_range_binder(v, filters) for k, v in ast.items()}
    return ast


def do_ast_rewriter(ast: list, temporal_filters: list, paramters: list, connection):
    # get the query type
    query_type = next(iter(ast))
    # bind the temporal ranges, we do that here because the order in the AST matters
    with_temporal_ranges = temporal_range_binder(ast, temporal_filters)
    # bind the user provided parameters, we this that here because we want it after the
    # AST has been created (to avoid injection flaws) but also because the order
    # matters
    with_parameters_exchanged = parameter_binder(
        with_temporal_ranges, parameter_set=paramters, connection=connection, query_type=query_type
    )
    if len(paramters) != 0:
        raise ParameterError("More parameters were provided than placeholders found in the query.")
    # Do some AST rewriting
    # first eliminate WHERE x IN (subquery) queries
    rewritten_query = with_parameters_exchanged

    return rewritten_query
