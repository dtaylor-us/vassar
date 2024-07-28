package org.vassar.api.port.`in`

import org.vassar.api.adapter.out.persistence.PersonNode
import reactor.core.publisher.Mono

interface LoadPersonUseCase {

    fun loadPerson(person: PersonNode): Mono<PersonNode>
}
