# -*- coding: utf-8 -*-

import typing as T
import moto
from boto_session_manager import BotoSesManager


class BaseTest:
    bucket: str = "111122223333-us-east-1-artifacts"
    mock_s3 = moto.mock_s3()
    mock_iam = moto.mock_iam()
    mock_cf = moto.mock_cloudformation()
    mock_sts = moto.mock_sts()
    bsm: T.Optional[BotoSesManager] = None

    @classmethod
    def setup_s3_bucket(cls):
        cls.bsm.s3_client.create_bucket(Bucket=cls.bucket)

    @classmethod
    def setup_class(cls):
        cls.mock_s3.start()
        cls.mock_iam.start()
        cls.mock_cf.start()
        cls.mock_sts.start()
        cls.bsm = BotoSesManager(region_name="us-east-1")

        cls.setup_s3_bucket()

    @classmethod
    def teardown_class(cls):
        cls.mock_s3.stop()
        cls.mock_iam.stop()
        cls.mock_cf.stop()
        cls.mock_sts.stop()