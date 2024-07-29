package org.vassar.api.port.`in`

import org.vassar.api.Postnomial
import org.vassar.api.adapter.out.persistence.PersonNode
import reactor.core.publisher.Mono

interface QueryPeopleUseCase {
    fun findByName(firstName: String, lastName: String, postnomial: Postnomial?): Mono<PersonNode>

    fun listAll(page: Int, size: Int): Mono<List<PersonNode>>
}
