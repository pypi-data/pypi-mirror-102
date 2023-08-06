from .base import EasycontrolCircuit
from bosch_thermostat_client.const import (
    NAME,
    STATUS,
    MODE_TO_SETPOINT,
    ID,
    ACTIVE_PROGRAM,
    URI,
)
from bosch_thermostat_client.const.easycontrol import TARGET_TEMP
from bosch_thermostat_client.operation_mode import EasyControlOperationModeHelper


class EasyZoneCircuit(EasycontrolCircuit):
    def __init__(
        self, connector, attr_id, db, _type, bus_type, current_date=None, **kwargs
    ):
        super().__init__(connector, attr_id, db, _type, bus_type, current_date)
        self._op_mode = EasyControlOperationModeHelper(
            self.name, self._db.get(MODE_TO_SETPOINT)
        )

        self._zone_program = kwargs.get("zone_program")

    @property
    def name(self):
        name = self.get_value(NAME)
        return name if name else super().name

    @property
    def schedule(self):
        """Easy control might not need schedule."""
        return None

    async def initialize(self):
        """Check each uri if return json with values."""
        await self.update_requested_key(STATUS)
        await self.update_requested_key(NAME)

    async def update(self):
        await self._zone_program.update()
        await super().update()

    @property
    def target_temperature(self):
        """Get target temperature of Circtuit. Temporary or Room set point."""
        if self._op_mode.is_off:
            self._target_temp = 0
            return self._target_temp
        target_temp = self.get_value(TARGET_TEMP, 0)
        if target_temp > 0:
            self._target_temp = target_temp
            return self._target_temp

    @property
    def support_presets(self):
        return True

    @property
    def preset_modes(self):
        return self._zone_program.preset_names

    def get_activeswitchprogram(self):
        """
        Retrieve active program from thermostat.
        If ActiveSwitch program is not present
        then take first one from the list from result.
        """
        if len(self._program_list) > 0:
            active_id = self.get_value(ACTIVE_PROGRAM)
            for program in self._program_list:
                if active_id == program[ID]:
                    return program[NAME]

    @property
    def preset_mode(self):
        return self._zone_program.preset_name(self.get_value(ACTIVE_PROGRAM))

    async def set_preset_mode(self, preset_mode):
        preset_id = self._zone_program.get_preset_index_by_name(preset_mode)
        act_program = self._data.get(ACTIVE_PROGRAM, {})
        active_program_uri = act_program[URI]
        result = await self._connector.put(active_program_uri, preset_id)
        await self.update_requested_key(ACTIVE_PROGRAM)
        return result
