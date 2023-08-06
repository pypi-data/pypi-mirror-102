from typing import Optional

from fastapi import APIRouter, Path, Query

from ..const import *
from ..data_models import *
from ..helpers import *
from ..main import _LOGGER, app, bbc

router = APIRouter()

# private API


@router.get("/query/{table_name}/{query}", include_in_schema=False)
async def get_query_results(
    table_name: TableName = Path(..., description="DB Table name"),
    query: str = Path(
        None, description="DB query to perform with placeholders for values"
    ),
    query_val: List[str] = Query(None, description="Values to populate DB query with"),
    columns: Optional[List[str]] = Query(
        None, description="Column names to include in the query result"
    ),
    limit: int = Query(None, description="number of rows returned by the query"),
):
    """
    Return query results with provided table name and query string
    """
    if columns:
        assert_table_columns_match(bbc=bbc, table_name=table_name, columns=columns)
    if isinstance(query_val, str):
        query_val = [query_val]
    try:
        return getattr(bbc, table_name2attr(table_name)).select(
            condition=query, condition_val=query_val, columns=columns, limit=limit
        )
    except Exception as e:
        msg = f"Caught exception while querying the DB: {str(e)}"
        _LOGGER.error(msg)
        raise HTTPException(status_code=404, detail=msg)


@router.get("/filters/{table_name}", include_in_schema=False)
async def get_search_setup_for_table(
    table_name: TableName = Path(..., description="DB Table name")
):
    """
    Returns the filters mapping to based on the selected table schema to
    construct the queryBuilder to interface the DB
    """
    if table_name.value == BED_TABLE:
        return get_search_setup(bbc.bed.schema)
    return get_search_setup(bbc.bedset.schema)
