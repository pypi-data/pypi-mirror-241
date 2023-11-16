# -*- coding: utf-8 -*-


class StackNotExistError(Exception):
    pass


class DeployStackFailedError(Exception):
    pass


class DeleteStackFailedError(Exception):
    pass


class CreateStackChangeSetButNotChangeError(Exception):
    pass


class CreateStackChangeSetFailedError(Exception):
    pass


class DeployStackInstanceFailedError(Exception):
    pass
