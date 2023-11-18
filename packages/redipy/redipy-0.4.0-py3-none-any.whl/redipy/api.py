"""This module defines the basic redis API. All redis functions appear once
in RedisAPI and once in PipelineAPI. Additional functionality is added via
RedisClientAPI."""
import contextlib
import datetime
from collections.abc import Iterator
from typing import Literal, overload

from redipy.backend.backend import ExecFunction
from redipy.symbolic.seq import FnContext


RSetMode = Literal[
    "always",
    "if_missing",  # NX
    "if_exists",  # XX
]
"""The conditions on when to set a value for the set command."""
RSM_ALWAYS: RSetMode = "always"
"""The value will always be set."""
RSM_MISSING: RSetMode = "if_missing"
"""The value will only be set when the key was missing.
This is equivalent to the NX flag."""
RSM_EXISTS: RSetMode = "if_exists"
"""The value will only be set when the key did exist.
This is equivalent to the XX flag."""


class PipelineAPI:
    """Redis API as pipeline. All methods return None and you have to call
    execute to retrieve the results of the pipeline commands."""
    def execute(self) -> list:
        """
        Executes the pipeline and returns the result values of each command.

        Returns:
            list: The result values of each command.
        """
        raise NotImplementedError()

    def exists(self, *keys: str) -> None:
        """
        Determines whether specified keys exist.

        See also the redis documentation: https://redis.io/commands/exists/

        The pipeline value is set to the number of keys that exist.

        Args:
            *keys (str): The keys.
        """
        raise NotImplementedError()

    def delete(self, *keys: str) -> None:
        """
        Deletes keys.

        See also the redis documentation: https://redis.io/commands/del/

        The pipeline value is set to the number of keys that got removed.

        Args:
            *keys (str): The keys.
        """
        raise NotImplementedError()

    def set(
            self,
            key: str,
            value: str,
            *,
            mode: RSetMode = RSM_ALWAYS,
            return_previous: bool = False,
            expire_timestamp: datetime.datetime | None = None,
            expire_in: float | None = None,
            keep_ttl: bool = False) -> None:
        """
        Sets a value for a given key. The value can be scheduled to expire.

        See also the redis documentation: https://redis.io/commands/set/

        The pipeline value depends on the return_previous argument.

        Args:
            key (str): The key.

            value (str): The value.

            mode (RSetMode, optional): Under which condition to set the value
            valid values are RSM_ALWAYS, RSM_MISSING, and RSM_EXISTS.
            RSM_MISSING is the equivalent of setting the NX flag. RSM_EXISTS is
            the equivalent of the XX flag. Defaults to RSM_ALWAYS.

            return_previous (bool, optional): Whether to return the previous
            value associated with the key. Defaults to False.

            expire_timestamp (datetime.datetime | None, optional): A timestamp
            on when to expire the key. Defaults to None.

            expire_in (float | None, optional): A relative time in seconds on
            when to expire the key. Defaults to None.

            keep_ttl (bool, optional): Whether to keep previous expiration
            times. Defaults to False.
        """
        raise NotImplementedError()

    def get(self, key: str) -> None:
        """
        Retrieves the value for the given key.

        See also the redis documentation: https://redis.io/commands/get/

        The pipeline value is the value or None if the key does not exists or
        the value has expired.

        Args:
            key (str): The key.
        """
        raise NotImplementedError()

    def incrby(self, key: str, inc: float | int) -> None:
        """
        Updates the value associated with the given key by a relative amount.
        The value is interpreted as number. If the value doesn't exist zero is
        used as starting point.

        See also the redis documentation:
        https://redis.io/commands/incrby/
        https://redis.io/commands/incrbyfloat/

        The pipeline value is set to the new value as float.
        If the value cannot be interpreted as float while executing the
        pipeline a ValueError exception is raised.

        Args:
            key (str): The key.

            inc (float | int): The relative change.
        """
        raise NotImplementedError()

    def lpush(self, key: str, *values: str) -> None:
        """
        Pushes values to the left side of the list associated with the key.

        See also the redis documentation: https://redis.io/commands/lpush/

        The pipeline value is the length of the list after the push.

        Args:
            key (str): The key.

            *values (str): The values to push.
        """
        raise NotImplementedError()

    def rpush(self, key: str, *values: str) -> None:
        """
        Pushes values to the right side of the list associated with the key.

        See also the redis documentation: https://redis.io/commands/rpush/

        The pipeline value is the length of the list after the push.

        Args:
            key (str): The key.

            *values (str): The values to push.
        """
        raise NotImplementedError()

    def lpop(
            self,
            key: str,
            count: int | None = None) -> None:
        """
        Pops a number of values from the left side of the list associated with
        the key.

        See also the redis documentation: https://redis.io/commands/lpop/

        The pipeline value is None if the key doesn't exist. If a count
        is set a list with values in pop order is set as pipeline value (even
        if it is set to one). If count is not set (default or None) the single
        value that got popped is set as pipeline value.

        Args:
            key (str): The key.

            count (int | None, optional): The number values to pop.
            Defaults to a single value.
        """
        raise NotImplementedError()

    def rpop(
            self,
            key: str,
            count: int | None = None) -> None:
        """
        Pops a number of values from the right side of the list associated with
        the key.

        See also the redis documentation: https://redis.io/commands/rpop/

        The pipeline value is None if the key doesn't exist. If a count
        is set a list with values in pop order is set as pipeline value (even
        if it is set to one). If count is not set (default or None) the single
        value that got popped is set as pipeline value.

        Args:
            key (str): The key.

            count (int | None, optional): The number values to pop.
            Defaults to a single value.
        """
        raise NotImplementedError()

    def lrange(self, key: str, start: int, stop: int) -> None:
        """
        Returns a number of values from the list specified by the given range.
        Negative numbers are interpreted as index from the back of the list.
        Out of range indices are ignored, potentially returning an empty list.

        See also the redis documentation: https://redis.io/commands/lrange/

        The pipeline value is the resulting elements.

        Args:
            key (str): The key.

            start (int): The start index.

            stop (int): The stop index (inclusive).
        """
        raise NotImplementedError()

    def llen(self, key: str) -> None:
        """
        Computes the length of the list associated with the key.

        See also the redis documentation: https://redis.io/commands/llen/

        The length of the list is set as pipeline value.

        Args:
            key (str): The key.
        """
        raise NotImplementedError()

    def zadd(self, key: str, mapping: dict[str, float]) -> None:
        """
        Adds elements to the sorted set associated with the key.

        See also the redis documentation: https://redis.io/commands/zadd/

        NOTE: not all setting modes are implemented yet.

        The number of new members is set as pipeline value.

        Args:
            key (str): The key.
            mapping (dict[str, float]): A dictionary with values and scores.
        """
        raise NotImplementedError()

    def zpop_max(
            self,
            key: str,
            count: int = 1,
            ) -> None:
        """
        Pops a number of members of the sorted set associated with the given
        key with the highest scores.

        See also the redis documentation: https://redis.io/commands/zpopmax/

        The members with their associated scores in pop order is set as
        pipeline value.

        Args:
            key (str): The key.

            count (int, optional): The number of members to remove.
            Defaults to 1.
        """
        raise NotImplementedError()

    def zpop_min(
            self,
            key: str,
            count: int = 1,
            ) -> None:
        """
        Pops a number of members of the sorted set associated with the given
        key with the lowest scores.

        See also the redis documentation: https://redis.io/commands/zpopmin/

        The members with their associated scores in pop order is set as
        pipeline value.

        Args:
            key (str): The key.

            count (int, optional): The number of members to remove.
            Defaults to 1.
        """
        raise NotImplementedError()

    def zrange(self, key: str, start: int, stop: int) -> None:
        """
        Returns a number of values from the sorted set specified by the given
        range. As of now the indices are based on the order of the set.
        Negative numbers are interpreted as index from the back of the set.
        Out of range indices are ignored, potentially returning an empty set.

        See also the redis documentation: https://redis.io/commands/zrange/

        NOTE: not all modes are implemented yet.

        The members names are set as pipeline value.

        Args:
            key (str): The key.

            start (int): The start index.

            stop (int): The stop index (inclusive).
        """
        raise NotImplementedError()

    def zcard(self, key: str) -> None:
        """
        Computes the cardinality of the sorted set associated with the given
        key.

        See also the redis documentation: https://redis.io/commands/zcard/

        The number of members in the set is set as pipeline value.

        Args:
            key (str): The key.
        """
        raise NotImplementedError()

    def hset(self, key: str, mapping: dict[str, str]) -> None:
        """
        Sets a mapping for the given hash.

        See also the redis documentation: https://redis.io/commands/hset/

        The pipeline value is set to the number of fields added.

        Args:
            key (str): The key.

            mapping (dict[str, str]): The field value pairs to be set.
        """
        raise NotImplementedError()

    def hdel(self, key: str, *fields: str) -> None:
        """
        Deletes fields from the given hash.

        See also the redis documentation: https://redis.io/commands/hdel/

        The pipeline value is set to the number of fields that got deleted
        (excluding fields that did not exist).

        Args:
            key (str): The key.

            *fields (str): The fields to delete.
        """
        raise NotImplementedError()

    def hget(self, key: str, field: str) -> None:
        """
        Retrieves the value associated with a field of a hash.

        See also the redis documentation: https://redis.io/commands/hget/

        The pipeline value is set to the value of the field or None if the
        field doesn't exist.

        Args:
            key (str): The key.

            field (str): The field.
        """
        raise NotImplementedError()

    def hmget(self, key: str, *fields: str) -> None:
        """
        Retrieves the values associated with given fields of a hash.

        See also the redis documentation: https://redis.io/commands/hmget/

        The pipeline value is set to a dictionary with fields mapping to their
        values. If a field doesn't exist in the hash the value is returned
        as None.

        Args:
            key (str): The key.

            *fields (str): The fields to retrieve.
        """
        raise NotImplementedError()

    def hincrby(self, key: str, field: str, inc: float | int) -> None:
        """
        Interprets a field value of a hash as number and updates the value.

        See also the redis documentation:
        https://redis.io/commands/hincrby/
        https://redis.io/commands/hincrbyfloat/

        The pipeline value is set to the new value of the field.

        Args:
            key (str): The key.

            field (str): The field to interpret as number.

            inc (float | int): The relative numerical change.
        """
        raise NotImplementedError()

    def hkeys(self, key: str) -> None:
        """
        Retrieves the fields of a hash.

        See also the redis documentation: https://redis.io/commands/hkeys/

        The pipeline value is set to a list of all fields of the given hash.

        Args:
            key (str): The key.
        """
        raise NotImplementedError()

    def hvals(self, key: str) -> None:
        """
        Retrieves the values of a hash.

        See also the redis documentation: https://redis.io/commands/hvals/

        The pipeline value is set to a list of all values of the given hash.

        Args:
            key (str): The key.
        """
        raise NotImplementedError()

    def hgetall(self, key: str) -> None:
        """
        Retrieves all fields and values of a hash.

        See also the redis documentation: https://redis.io/commands/hgetall/

        The pipeline value is set to a dictionary with fields mapping to their
        values.

        Args:
            key (str): The key.
        """
        raise NotImplementedError()


class RedisAPI:
    """The redis API."""
    def exists(self, *keys: str) -> int:
        """
        Determines whether specified keys exist.

        See also the redis documentation: https://redis.io/commands/exists/

        Args:
            *keys (str): The keys.

        Returns:
            int: The number of keys that exist.
        """
        raise NotImplementedError()

    def delete(self, *keys: str) -> int:
        """
        Deletes keys.

        See also the redis documentation: https://redis.io/commands/del/

        Args:
            *keys (str): The keys.

        Returns:
            int: The number of keys that got removed.
        """
        raise NotImplementedError()

    @overload
    def set(
            self,
            key: str,
            value: str,
            *,
            mode: RSetMode,
            return_previous: Literal[True],
            expire_timestamp: datetime.datetime | None,
            expire_in: float | None,
            keep_ttl: bool) -> str | None:
        ...

    @overload
    def set(
            self,
            key: str,
            value: str,
            *,
            mode: RSetMode,
            return_previous: Literal[False],
            expire_timestamp: datetime.datetime | None,
            expire_in: float | None,
            keep_ttl: bool) -> bool | None:
        ...

    @overload
    def set(
            self,
            key: str,
            value: str,
            *,
            mode: RSetMode = RSM_ALWAYS,
            return_previous: bool = False,
            expire_timestamp: datetime.datetime | None = None,
            expire_in: float | None = None,
            keep_ttl: bool = False) -> str | bool | None:
        ...

    def set(
            self,
            key: str,
            value: str,
            *,
            mode: RSetMode = RSM_ALWAYS,
            return_previous: bool = False,
            expire_timestamp: datetime.datetime | None = None,
            expire_in: float | None = None,
            keep_ttl: bool = False) -> str | bool | None:
        """
        Sets a value for a given key. The value can be scheduled to expire.

        See also the redis documentation: https://redis.io/commands/set/

        Args:
            key (str): The key.

            value (str): The value.

            mode (RSetMode, optional): Under which condition to set the value
            valid values are RSM_ALWAYS, RSM_MISSING, and RSM_EXISTS.
            RSM_MISSING is the equivalent of setting the NX flag. RSM_EXISTS is
            the equivalent of the XX flag. Defaults to RSM_ALWAYS.

            return_previous (bool, optional): Whether to return the previous
            value associated with the key. Defaults to False.

            expire_timestamp (datetime.datetime | None, optional): A timestamp
            on when to expire the key. Defaults to None.

            expire_in (float | None, optional): A relative time in seconds on
            when to expire the key. Defaults to None.

            keep_ttl (bool, optional): Whether to keep previous expiration
            times. Defaults to False.

        Returns:
            str | bool | None: The return value depends on the return_previous
            argument.
        """
        raise NotImplementedError()

    def get(self, key: str) -> str | None:
        """
        Retrieves the value for the given key.

        See also the redis documentation: https://redis.io/commands/get/

        Args:
            key (str): The key.

        Returns:
            str | None: The value or None if the key does not exists or the
            value has expired.
        """
        raise NotImplementedError()

    def incrby(self, key: str, inc: float | int) -> float:
        """
        Updates the value associated with the given key by a relative amount.
        The value is interpreted as number. If the value doesn't exist zero is
        used as starting point.

        See also the redis documentation:
        https://redis.io/commands/incrby/
        https://redis.io/commands/incrbyfloat/

        Args:
            key (str): The key.

            inc (float | int): The relative change.

        Raises:
            ValueError: If the value cannot be interpreted as float.

        Returns:
            float: The new value as float.
        """
        raise NotImplementedError()

    def lpush(self, key: str, *values: str) -> int:
        """
        Pushes values to the left side of the list associated with the key.

        See also the redis documentation: https://redis.io/commands/lpush/

        Args:
            key (str): The key.

            *values (str): The values to push.

        Returns:
            int: The length of the list after the push.
        """
        raise NotImplementedError()

    def rpush(self, key: str, *values: str) -> int:
        """
        Pushes values to the right side of the list associated with the key.

        See also the redis documentation: https://redis.io/commands/rpush/

        Args:
            key (str): The key.

            *values (str): The values to push.

        Returns:
            int: The length of the list after the push.
        """
        raise NotImplementedError()

    @overload
    def lpop(
            self,
            key: str,
            count: None = None) -> str | None:
        ...

    @overload
    def lpop(
            self,
            key: str,
            count: int) -> list[str] | None:
        ...

    def lpop(
            self,
            key: str,
            count: int | None = None) -> str | list[str] | None:
        """
        Pops a number of values from the left side of the list associated with
        the key.

        See also the redis documentation: https://redis.io/commands/lpop/

        Args:
            key (str): The key.

            count (int | None, optional): The number values to pop.
            Defaults to a single value.

        Returns:
            str | list[str] | None: None if the key doesn't exist. If a count
            is set a list with values in pop order is returned (even if it is
            set to one). If count is not set (default or None) the single value
            that got popped is returned.
        """
        raise NotImplementedError()

    @overload
    def rpop(
            self,
            key: str,
            count: None = None) -> str | None:
        ...

    @overload
    def rpop(
            self,
            key: str,
            count: int) -> list[str] | None:
        ...

    def rpop(
            self,
            key: str,
            count: int | None = None) -> str | list[str] | None:
        """
        Pops a number of values from the right side of the list associated with
        the key.

        See also the redis documentation: https://redis.io/commands/rpop/

        Args:
            key (str): The key.

            count (int | None, optional): The number values to pop.
            Defaults to a single value.

        Returns:
            str | list[str] | None: None if the key doesn't exist. If a count
            is set a list with values in pop order is returned (even if it is
            set to one). If count is not set (default or None) the single value
            that got popped is returned.
        """
        raise NotImplementedError()

    def lrange(self, key: str, start: int, stop: int) -> list[str]:
        """
        Returns a number of values from the list specified by the given range.
        Negative numbers are interpreted as index from the back of the list.
        Out of range indices are ignored, potentially returning an empty list.

        See also the redis documentation: https://redis.io/commands/lrange/

        Args:
            key (str): The key.

            start (int): The start index.

            stop (int): The stop index (inclusive).

        Returns:
            list[str]: The elements.
        """
        raise NotImplementedError()

    def llen(self, key: str) -> int:
        """
        Computes the length of the list associated with the key.

        See also the redis documentation: https://redis.io/commands/llen/

        Args:
            key (str): The key.

        Returns:
            int: The length of the list.
        """
        raise NotImplementedError()

    def zadd(self, key: str, mapping: dict[str, float]) -> int:
        """
        Adds elements to the sorted set associated with the key.

        See also the redis documentation: https://redis.io/commands/zadd/

        NOTE: not all setting modes are implemented yet.

        Args:
            key (str): The key.
            mapping (dict[str, float]): A dictionary with values and scores.

        Returns:
            int: The number of new members.
        """
        raise NotImplementedError()

    def zpop_max(
            self,
            key: str,
            count: int = 1,
            ) -> list[tuple[str, float]]:
        """
        Pops a number of members of the sorted set associated with the given
        key with the highest scores.

        See also the redis documentation: https://redis.io/commands/zpopmax/

        Args:
            key (str): The key.

            count (int, optional): The number of members to remove.
            Defaults to 1.

        Returns:
            list[tuple[str, float]]: The members with their associated scores
            in pop order.
        """
        raise NotImplementedError()

    def zpop_min(
            self,
            key: str,
            count: int = 1,
            ) -> list[tuple[str, float]]:
        """
        Pops a number of members of the sorted set associated with the given
        key with the lowest scores.

        See also the redis documentation: https://redis.io/commands/zpopmin/

        Args:
            key (str): The key.

            count (int, optional): The number of members to remove.
            Defaults to 1.

        Returns:
            list[tuple[str, float]]: The members with their associated scores
            in pop order.
        """
        raise NotImplementedError()

    def zrange(self, key: str, start: int, stop: int) -> list[str]:
        """
        Returns a number of values from the sorted set specified by the given
        range. As of now the indices are based on the order of the set.
        Negative numbers are interpreted as index from the back of the set.
        Out of range indices are ignored, potentially returning an empty set.

        See also the redis documentation: https://redis.io/commands/zrange/

        NOTE: not all modes are implemented yet.

        Args:
            key (str): The key.

            start (int): The start index.

            stop (int): The stop index (inclusive).

        Returns:
            list[str]: The members names.
        """
        raise NotImplementedError()

    def zcard(self, key: str) -> int:
        """
        Computes the cardinality of the sorted set associated with the given
        key.

        See also the redis documentation: https://redis.io/commands/zcard/

        Args:
            key (str): The key.

        Returns:
            int: The number of members in the set.
        """
        raise NotImplementedError()

    def hset(self, key: str, mapping: dict[str, str]) -> int:
        """
        Sets a mapping for the given hash.

        See also the redis documentation: https://redis.io/commands/hset/

        Args:
            key (str): The key.

            mapping (dict[str, str]): The field value pairs to be set.

        Returns:
            int: The number of fields added.
        """
        raise NotImplementedError()

    def hdel(self, key: str, *fields: str) -> int:
        """
        Deletes fields from the given hash.

        See also the redis documentation: https://redis.io/commands/hdel/

        Args:
            key (str): The key.

            *fields (str): The fields to delete.

        Returns:
            int: The number of fields that got deleted (excluding fields that
            did not exist).
        """
        raise NotImplementedError()

    def hget(self, key: str, field: str) -> str | None:
        """
        Retrieves the value associated with a field of a hash.

        See also the redis documentation: https://redis.io/commands/hget/

        Args:
            key (str): The key.

            field (str): The field.

        Returns:
            str | None: The value of the field or None if the field doesn't
            exist.
        """
        raise NotImplementedError()

    def hmget(self, key: str, *fields: str) -> dict[str, str | None]:
        """
        Retrieves the values associated with given fields of a hash.

        See also the redis documentation: https://redis.io/commands/hmget/

        Args:
            key (str): The key.

            *fields (str): The fields to retrieve.

        Returns:
            dict[str, str | None]: A dictionary with fields mapping to their
            values. If a field doesn't exist in the hash the value is returned
            as None.
        """
        raise NotImplementedError()

    def hincrby(self, key: str, field: str, inc: float | int) -> float:
        """
        Interprets a field value of a hash as number and updates the value.

        See also the redis documentation:
        https://redis.io/commands/hincrby/
        https://redis.io/commands/hincrbyfloat/

        Args:
            key (str): The key.

            field (str): The field to interpret as number.

            inc (float | int): The relative numerical change.

        Returns:
            float: The new value of the field.
        """
        raise NotImplementedError()

    def hkeys(self, key: str) -> list[str]:
        """
        Retrieves the fields of a hash.

        See also the redis documentation: https://redis.io/commands/hkeys/

        Args:
            key (str): The key.

        Returns:
            list[str]: All fields of the given hash.
        """
        raise NotImplementedError()

    def hvals(self, key: str) -> list[str]:
        """
        Retrieves the values of a hash.

        See also the redis documentation: https://redis.io/commands/hvals/

        Args:
            key (str): The key.

        Returns:
            list[str]: All values of the given hash.
        """
        raise NotImplementedError()

    def hgetall(self, key: str) -> dict[str, str]:
        """
        Retrieves all fields and values of a hash.

        See also the redis documentation: https://redis.io/commands/hgetall/

        Args:
            key (str): The key.

        Returns:
            dict[str, str]: A dictionary with fields mapping to their values.
        """
        raise NotImplementedError()


class RedisClientAPI(RedisAPI):
    """This class enriches the redis API with pipeline and script
    functionality."""
    @contextlib.contextmanager
    def pipeline(self) -> Iterator[PipelineAPI]:
        """
        Starts a redis pipeline. When leaving the resource block the pipeline
        is executed automatically and the results are discarded. If you need
        the results call execute on the pipeline object.

        Yields:
            PipelineAPI: The pipeline.
        """
        raise NotImplementedError()

    def register_script(self, ctx: FnContext) -> ExecFunction:
        """
        Registers a script that can be executed in this redis runtime.

        Args:
            ctx (FnContext): The script to register.

        Returns:
            ExecFunction: A python that can be called to execute the script.
        """
        raise NotImplementedError()
