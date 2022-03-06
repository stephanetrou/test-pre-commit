import re
import sqlalchemy
from testcontainers.core.container import DockerContainer
from testcontainers.postgres import PostgresContainer
from testcontainers.kafka import KafkaContainer

class SqitchContainer(DockerContainer):
    def __init__(self, image) -> None:
        super(SqitchContainer, self).__init__(image)
        self.with_command("./sqitch help")


def main():
    reg = re.compile("^\[[A-Z]{2,5}\-\d+\]\s.*$")

    print(reg.match("[JIRA-1223]Hello world"))
    print(reg.match("[JIRA-1223] Hello world"))

    with PostgresContainer("postgres:10.1") as postgres, KafkaContainer() as kafka, SqitchContainer("sqitch/sqitch:latest") as sqitch:
        print(kafka.get_bootstrap_server())
        e = sqlalchemy.create_engine(postgres.get_connection_url())
        result = e.execute("select version()").fetchone()
        print(result)


if __name__ == "__main__":
    main()
