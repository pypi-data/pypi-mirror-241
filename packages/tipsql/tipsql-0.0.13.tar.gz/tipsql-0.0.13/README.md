# Type Safed SQL Query Builder for Python

[![test](https://github.com/yassun7010/tipsql/actions/workflows/test-suite.yml/badge.svg)](https://github.com/yassun7010/tipsql/actions)
[![pypi package](https://badge.fury.io/py/tipsql.svg)](https://pypi.org/project/tipsql)

## Development Notes
### DDL

There are no plans for support.

DDL is often used infrequently as its syntax varies from database to database.
It is recommended that it be managed by a separate migration tool.

### For Table Relation

If a PrimaryKey or a join key is included as a constraint, it can be expressed as a NewType
to match the condition.

## Examples

```py
from textwrap import dedent

from tipsql.core.query.builder import QueryBuilder

from your_project.database.public import User, Address


builder = (
    query.chain()
    .from_(
        lambda c: c(User)
        .left_outer_join(
            Address,
        )
        .on(
            lambda c: c(User.id == Address.user_id)
            .and_(Address.city == "Tokyo")
        )
    )
    .select(
        User.id,
        User.name,
    )
)

assert (
    builder.build()
    == dedent(
        """
        SELECT
            users.id,
            users.name
        FROM
            users
            LEFT OUTER JOIN
                addresses
            ON
                users.id = addresses.user_id
                AND addresses.city = 'Tokyo';
        """
    ).strip()
)
```
