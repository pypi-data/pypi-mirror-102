# PDP Kafka Reader

## Requirements

* git
* python 3.6+
* pip

Also, you need access to the git repository. Generate and use ssh keys in Skyway Bitbucket.

## Install

```bash
pip install pdp_kafka_reader
```

## Usage

### CLI

You can use `kafka-csv-export` CLI tool to extract avro data into csv from a specific avro topic. An example of usage:

```bash
kafka-csv-export -k kafka-options.json -s schema.json -t my_kafka_topic -o out.csv
```

### Python KafkaReader

```python
import json

from pdp_kafka_reader.kafka_reader import KafkaAvroReader

kafka_options = {
    "kafka.bootstrap.servers": "my-kafka-server:9092",
    "subscribe": "test_avro"
}

avro_schema = open("schema.json").read()

reader = KafkaAvroReader(spark)
df = reader.read_avro(kafka_options, avro_schema, "my_kafka_topic")
df.show()
```

## Testing

Testing environment in defined in `docker-compose.yml`. Start docker containers and run `tox`.