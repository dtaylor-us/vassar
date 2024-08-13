package org.vassar.api.port.out

import org.vassar.api.domain.Postnomial
import org.vassar.api.adapter.out.persistence.PersonNode
import reactor.core.publisher.Mono

interface PersonPort {
    fun loadPerson(person: PersonNode): Mono<PersonNode>
    fun findByName(firstName: String, lastName: String, postnomial: Postnomial?): Mono<PersonNode>
//    fun listAll(page: Int, size: Int): Mono<List<PersonNode>>
    fun getGenealogyTree(): Mono<List<PersonNode>>
    fun deleteAll(): Any
}
