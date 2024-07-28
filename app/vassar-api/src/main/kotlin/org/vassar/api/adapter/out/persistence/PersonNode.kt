package org.vassar.api.adapter.out.persistence

import org.springframework.data.neo4j.core.schema.GeneratedValue
import org.springframework.data.neo4j.core.schema.Id
import org.springframework.data.neo4j.core.schema.Node
import org.springframework.data.neo4j.core.schema.Relationship
import org.vassar.api.Postnomial
import java.time.LocalDate

@Node("Person")
data class PersonNode(
    @Id @GeneratedValue val id: String? = null,
    val firstName: String,
    val lastName: String,
    val email: Email? = null,
    val postnomial: Postnomial,
    val birthdate: LocalDate,
    val deathOfDate: LocalDate? = null,
    val occupation: List<String>,
    val bio: String,
    val gender: Gender,
    @Relationship(type = "PARENT_OF", direction = Relationship.Direction.OUTGOING)
    var children: List<PersonNode> = listOf(),
    @Relationship(type = "CHILD_OF", direction = Relationship.Direction.INCOMING)
    var parents: List<PersonNode> = listOf(),
    @Relationship(type = "SPOUSE", direction = Relationship.Direction.OUTGOING)
    var spouse: PersonNode? = null
)
