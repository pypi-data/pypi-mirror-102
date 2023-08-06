from typing import List
from box import Box
from injecta.dtype.DType import DType
from injecta.package.path_resolver import resolve_path
from injecta.service.Service import Service
from injecta.service.ServiceAlias import ServiceAlias
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from loggerbundle.LoggerFactory import LoggerFactory
from pyfonycore.bootstrap.config.config_reader import read  # noqa: F401
from pyfonybundles.Bundle import Bundle


def _create_logger():
    logger_service = Service("daipecore.logger", DType("logging", "Logger"), [PrimitiveArgument("daipecore")])
    logger_service.set_factory(ServiceArgument(LoggerFactory.__module__), "create")

    return logger_service


class DaipeCore(Bundle):

    config_reader = read
    logger_service = _create_logger()

    def modify_raw_config(self, raw_config: dict) -> dict:
        bootstrap_config = DaipeCore.config_reader()

        if "daipe" in raw_config["parameters"]:
            raise Exception("parameters.daipe must not be explicitly defined")

        raw_config["parameters"]["daipe"] = {
            "root_module": {
                "name": bootstrap_config.root_module_name,
                "path": resolve_path(bootstrap_config.root_module_name).replace("\\", "/"),
            }
        }

        return raw_config

    def modify_services(self, services: List[Service], aliases: List[ServiceAlias], parameters: Box):
        services.append(DaipeCore.logger_service)

        return services, aliases
