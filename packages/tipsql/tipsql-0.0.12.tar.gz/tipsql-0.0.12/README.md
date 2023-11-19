# 型安全な SQL クエリビルダー

## DDL

サポートしない。DMLのみを対象にする。

DDL は構文がデータベースごとに異なることが多く、使用頻度も少ない。
別のマイグレーションツールで管理することを推奨する。

## 関連テーブルについて

PrimaryKey や結合キーが制約として含まれている場合、 NewType
で表現することで条件の一致を行わせる。

## 実例

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
