package org.vassar.api.adapter.out.persistence

import org.springframework.data.neo4j.core.schema.Id
import org.springframework.data.neo4j.core.schema.Node
import org.springframework.data.neo4j.core.schema.Relationship


@Node("Sister")
data class SisterNode(
    @Id val id: String,
    @Relationship(type = "PERSON", direction = Relationship.Direction.OUTGOING)
    val person: PersonNode,
    val education: String,
    @Relationship(type = "HUSBAND_OF", direction = Relationship.Direction.INCOMING)
    val husband: PersonNode?,
    @Relationship(type = "MOTHER_OF", direction = Relationship.Direction.OUTGOING)
    val children: List<PersonNode> = listOf()
)
