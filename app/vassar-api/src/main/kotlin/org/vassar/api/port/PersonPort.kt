package org.vassar.api.port

import org.vassar.api.Postnomial
import org.vassar.api.adapter.out.persistence.PersonNode
import reactor.core.publisher.Mono

interface PersonPort {
    fun loadPerson(person: PersonNode): Mono<PersonNode>
    fun findByName(firstName: String, lastName: String, postnomial: Postnomial?): Mono<PersonNode>
}
