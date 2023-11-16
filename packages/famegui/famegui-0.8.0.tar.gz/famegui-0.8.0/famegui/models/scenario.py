import logging
import typing
from typing import List

import fameio.source.scenario as fameio
import fameio.source.schema as fameio_schema
from fameio.source.scenario import Contract, Attribute

import famegui.models as models


class Scenario(fameio.Scenario):
    def __init__(self, schema: fameio_schema.Schema, props: fameio.GeneralProperties):
        super().__init__(schema, props)

    @property
    def contracts(self) -> List[Contract]:
        return super().contracts

    def del_all_related_contracts(self, agent_id: int) -> None:
        """Delete all contracts related to the given agent"""
        contracts_to_delete = []
        for idx, contract in enumerate(super().contracts[:]):
            if contract.sender_id == agent_id or contract.receiver_id == agent_id:
                contracts_to_delete.append(contract)
        for contract in contracts_to_delete:
            super().contracts.remove(contract)

    def set_agent_display_xy(self, agent_id: int, x: int, y: int) -> None:
        for a in self.agents:
            if a.id == agent_id:
                a.set_display_xy(x, y)
                return
        raise RuntimeError(f"Unknown agent with ID '{agent_id}'")

    def update_properties(self, props: models.GeneralProperties) -> bool:
        """Sync the scenario properties with the given ones, returns True if some changes"""
        if props.to_dict() != self.general_properties.to_dict():
            logging.info("Updating scenario general properties")
            self._general_props = props
            return True
        return False

    def get_amount_of_related_contracts(self, agent_id) -> int:
        """Return the amount of directly connected agents to the given agent_id"""
        amount = 0
        for contract in self.contracts:
            if contract.sender_id == agent_id or contract.receiver_id == agent_id:
                amount += 1
        return amount

    def get_amount_connected_agents(self, agent_id: int) -> int:
        """Return the amount of directly connected agents to the given agent_id"""
        agent_id_set = set()

        for contract in self.contracts:
            if contract.sender_id == agent_id:
                agent_id_set.add(contract.receiver_id)
                continue
            if contract.receiver_id == agent_id:
                agent_id_set.add(contract.sender_id)

        return len(agent_id_set)

    def get_agent_by_id(self, agent_id: int) -> models.Agent:
        """Return the agent object model with the given agent_id"""
        for agent in self.agents:
            if agent.id == agent_id:
                return agent
        raise RuntimeError(f"Unknown agent with ID '{agent_id}'")

    def get_all_related_agents_ids(self, agent_id: int) -> List[int]:
        """Return a list of all agents related to the given agent_id"""
        agent_id_set = set()

        for contract in self.contracts:
            if contract.sender_id == agent_id:
                agent_id_set.add(contract.receiver_id)
                continue
            if contract.receiver_id == agent_id:
                agent_id_set.add(contract.sender_id)

        return list(agent_id_set)

    def add_contract(self, contract: models.Contract) -> None:
        # TODO: move here the logic located in MainController._create_contract_model
        super().add_contract(contract)

    def update_agent(self, updated_agent: models.Agent) -> None:
        """Update the agent with the given updated_agent."""

        for idx, agent in enumerate(super().agents[:]):
            if agent.id == updated_agent.id:
                for attr, value in updated_agent.attributes.items():
                    if value == "" or value is None:
                        continue

                    super().agents[idx].attributes[attr] = Attribute(attr, value)

    def agent_exists(self, agent_id: int) -> bool:
        """Check if an agent with the given id exists in the scenario."""
        return any([True for agent in self.agents if agent.id == agent_id])

    def update_contract(
        self, old_contract: models.Contract, updated_contract: Contract
    ) -> None:
        """Update the contract with the given updated_contract."""
        """By searching the contract with the same product_name, sender_id 
        and receiver_id. to replace it with the updated_contract!!!"""

        # TODO: Far Future Exception: if a contract has empty required attributes

        for idx, contract in enumerate(super().contracts[:]):
            if (
                contract.product_name == old_contract.product_name
                and contract.sender_id == old_contract.sender_id
                and contract.receiver_id == old_contract.receiver_id
            ):
                super().contracts[idx] = updated_contract

    @property
    def agents(self) -> typing.List[models.Agent]:
        """Return the list of agents in the scenario."""
        return super().agents
