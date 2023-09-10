"""Support for LimitlessLED bulbs."""

import voluptuous

import homeassistant.components.limitlessled.light_rf as light_rf

from homeassistant.components.light import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as config_validation

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        voluptuous.Optional(light_rf.CONF_RADIO_SECTION): voluptuous.All(
            {
                voluptuous.Optional(
                    light_rf.CONF_RADIO_GPIO_PIN
                ): config_validation.positive_int,
                voluptuous.Optional(
                    light_rf.CONF_RADIO_SPI_BUS
                ): config_validation.positive_int,
                voluptuous.Optional(
                    light_rf.CONF_RADIO_SPI_DEV
                ): config_validation.positive_int,
                voluptuous.Optional(light_rf.CONF_RADIO_TYPE): config_validation.string,
            }
        ),
        voluptuous.Optional(
            light_rf.CONF_REMOTE_RETRIES
        ): config_validation.positive_int,
        voluptuous.Optional(light_rf.CONF_REMOTE_FORMAT): config_validation.match_all,
        voluptuous.Optional(light_rf.CONF_ZONE_FORMAT): config_validation.match_all,
        voluptuous.Optional(light_rf.CONF_REMOTES_SECTION): voluptuous.All(
            config_validation.ensure_list,
            [
                {
                    voluptuous.Optional(
                        light_rf.CONF_REMOTE_START
                    ): config_validation.positive_int,
                    voluptuous.Optional(
                        light_rf.CONF_REMOTE_TYPE
                    ): config_validation.string,
                    voluptuous.Optional(
                        light_rf.CONF_REMOTE_COUNT
                    ): config_validation.positive_int,
                    voluptuous.Optional(
                        light_rf.CONF_REMOTE_ZONES
                    ): config_validation.ensure_list,
                    voluptuous.Optional(
                        light_rf.CONF_REMOTE_RETRIES
                    ): config_validation.positive_int,
                    voluptuous.Optional(
                        light_rf.CONF_REMOTE_FORMAT
                    ): config_validation.match_all,
                    voluptuous.Optional(
                        light_rf.CONF_ZONE_FORMAT
                    ): config_validation.match_all,
                }
            ],
        ),
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Configure Home Assistant to be aware of all entities specified in the configuration file."""
    light_rf.setup_platform(hass, config, add_entities, discovery_info=discovery_info)
