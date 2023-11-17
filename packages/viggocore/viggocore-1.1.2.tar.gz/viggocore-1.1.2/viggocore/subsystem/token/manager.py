import uuid
import hashlib

from viggocore.common import exception
from viggocore.common.subsystem import manager
from viggocore.common.subsystem import operation


class Create(operation.Operation):

    def pre(self, **kwargs):
        # FIXME(samueldmq): this method needs to receive the parameters
        # explicitly.
        if kwargs.get('user'):
            # FIXME(samueldmq): how to avoid someone simply passing the user
            # in the body and then having a valid token?
            self.user = kwargs['user']
        else:
            domain_name = kwargs.get('domain_name', None)
            username = kwargs.get('username', None)
            email = kwargs.get('email', None)
            password = kwargs.get('password', None)
            password_hash = kwargs.get('password_hash', None)
            self.natureza = kwargs.get('natureza', None)

            # TODO(samueldmq): allow get by unique attrs
            domains = self.manager.api.domains().list(name=domain_name)

            if not domains:
                return False

            domain_id = domains[0].id
            if password_hash is None:
                password_hash = hashlib.sha256(
                    password.encode('utf-8')).hexdigest()

            if (email is None):
                users = self.manager.api.users().list(
                    domain_id=domain_id, name=username, password=password_hash)
            else:
                users = self.manager.api.users().list(
                    domain_id=domain_id, email=email, password=password_hash)

            if not users:
                return False

            self.user = users[0]
            if self.user.active is False:
                raise exception.PreconditionFailed('Usuário não está ativo!')

        return self.user.is_stable()

    def do(self, session, **kwargs):
        # TODO(samueldmq): use self.user.id instead of self.user_id
        token = self.driver.instantiate(
            id=uuid.uuid4().hex,
            created_by=self.user.id,
            user_id=self.user.id,
            natureza=self.natureza)

        self.driver.create(token, session=session)

        return token


class DeletarTokens(operation.Delete):

    def do(self, session, **kwargs):
        sql_query = """
            DELETE FROM token WHERE id <> '{}' AND user_id='{}'
        """
        session.execute(sql_query.format(self.entity.id, self.entity.user_id))


class Manager(manager.Manager):

    def __init__(self, driver):
        super().__init__(driver)
        self.create = Create(self)
        self.deletar_tokens = DeletarTokens(self)
