from unittest import mock

import pytest

from snowflake.core._internal.bridge.rest_errors import NotFound
from snowflake.core.database import Database, DatabaseCollection
from snowflake.core.database._generated.models.clone import Clone
from snowflake.core.database._generated.models.point_of_time_offset import PointOfTimeOffset
from snowflake.core.exceptions import NotFoundError, ServiceError


fake_root = mock.MagicMock()
dbs = DatabaseCollection(fake_root)


def test_fetch():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(NotFoundError):
            dbs["my_db"].fetch()
    mocked_execute.assert_called_once_with(
        "SHOW DATABASES LIKE 'my_db' "
    )

def test_create_clone():
    clone = Clone(
        source="other_db",
        point_of_time=PointOfTimeOffset(point_of_time_type="offset", reference="at", when="-1800"),
    )
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs.create(
                Database(
                    name="my_db",
                    comment="my comment",
                ),
                kind="transient",
                clone=clone,
            )
    mocked_execute.assert_called_once_with(
        "CREATE transient DATABASE my_db CLONE other_db AT OFFSET => -1800 COMMENT = 'my comment' "
    )

def test_create():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs.create(
                Database(
                    name="my_db",
                    comment="my comment",
                    max_data_extension_time_in_days=1,
                ),
                kind="transient",
            )
    mocked_execute.assert_called_once_with(
        "CREATE transient DATABASE my_db MAX_DATA_EXTENSION_TIME_IN_DAYS = 1 COMMENT = 'my comment' "
    )

def test_create_or_update_create():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with mock.patch(
            "snowflake.core._internal.bridge.resources.database_resource.DatabaseResource.desc_db",
            side_effect=NotFound(),
        ):
            with pytest.raises(ServiceError):
                dbs["new_db"].create_or_update(
                    Database(
                        name="new_db",
                        comment="new comment",
                        max_data_extension_time_in_days=1,
                    ),
                )
    mocked_execute.assert_called_once_with(
        "CREATE DATABASE new_db MAX_DATA_EXTENSION_TIME_IN_DAYS = 1 COMMENT = 'new comment' "
    )

def test_create_or_update_update():
    old_db = Database(
        name="db",
        comment="old comment",
        max_data_extension_time_in_days=0,
    )
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with mock.patch(
            "snowflake.core._internal.bridge.resources.database_resource.DatabaseResource.desc_db",
            return_value=("fake sql", old_db.to_dict()),
        ):
            with pytest.raises(ServiceError):
                dbs["db"].create_or_update(
                    Database(
                        name="db",
                        comment="new comment",
                        max_data_extension_time_in_days=1,
                    ),
                )
    mocked_execute.assert_called_once_with(
        "ALTER DATABASE db SET comment = 'new comment' max_data_extension_time_in_days = 1"
    )


def test_create_from_share():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs.create_from_share(
                name="my_own_db",
                share="share.db",
                kind="TRANSIENT",
            )
    mocked_execute.assert_called_once_with(
        "CREATE TRANSIENT DATABASE my_own_db FROM SHARE share.db "
    )

def test_delete():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs["my_db"].delete()
    mocked_execute.assert_called_once_with(
        "DROP DATABASE my_db"
    )

def test_enable_replication():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs["my_db"].enable_replication(
                accounts=["my_org.account2"],
            )
    mocked_execute.assert_called_once_with(
        "ALTER DATABASE my_db ENABLE REPLICATION TO ACCOUNTS my_org.account2",
    )

def test_disable_replication():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs["my_db"].disable_replication(
                accounts=["my_org.account2"],
            )
    mocked_execute.assert_called_once_with(
        "ALTER DATABASE my_db DISABLE REPLICATION TO ACCOUNTS my_org.account2",
    )

def test_refresh_replication():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs["my_db"].refresh_replication()
    mocked_execute.assert_called_once_with(
        "ALTER DATABASE my_db REFRESH",
    )

def test_enable_failover():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs["my_db"].enable_failover(
                accounts=["my_org.account2"],
            )
    mocked_execute.assert_called_once_with(
        "ALTER DATABASE my_db ENABLE FAILOVER TO ACCOUNTS my_org.account2",
    )

def test_disable_failover():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs["my_db"].disable_failover()
    mocked_execute.assert_called_once_with(
        "ALTER DATABASE my_db DISABLE FAILOVER ",
    )

def test_primary_failover():
    with mock.patch(
        "snowflake.core._internal.bridge.executor.SnowExecute.execute"
    ) as mocked_execute:
        with pytest.raises(ServiceError):
            dbs["my_db"].primary_failover()
    mocked_execute.assert_called_once_with(
        "ALTER DATABASE my_db PRIMARY",
    )
