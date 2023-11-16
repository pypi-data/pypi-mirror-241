# -*- coding: utf-8 -*-

import pytest
from aws_cloudformation.waiter import Waiter


class TestWaiter:
    def test(self):
        with pytest.raises(TimeoutError):
            for _ in Waiter(
                delays=1,
                timeout=3,
                # verbose=True,
                verbose=False,
            ):
                pass


if __name__ == "__main__":
    from aws_cloudformation.tests import run_cov_test

    run_cov_test(__file__, "aws_cloudformation.waiter", preview=False)
