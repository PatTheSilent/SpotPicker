# Spot Picker

## Overview

This tool will fetch interruption frequencies from [AWS Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/) and send them to one of the supported data backends. You can use this information to observe interruption rates for your instance types and for alerts if they're being interrupted more frequently.

## Building

```
docker build .
```

## Development

### Starting a development stack
```
docker-compose up -d
```

## TODO

- [x] InfluxDB support
- [x] ElasticSearch support
- [ ] Helm Chart
- [ ] Example IAM policy
- [ ] Docker image
- [ ] HTTPS and auth handling for Elasticsearch
- [ ] Multithreading - avoid blocking sends between data backends