package org.vassar.api.port.`in`

import org.vassar.api.domain.Postnomial
import org.vassar.api.adapter.out.persistence.PersonNode
import reactor.core.publisher.Mono

interface QueryPeopleUseCase {
    fun findByName(firstName: String, lastName: String, postnomial: Postnomial?): Mono<PersonNode>


    fun getGenealogyTree(): Mono<List<PersonNode>>
}
