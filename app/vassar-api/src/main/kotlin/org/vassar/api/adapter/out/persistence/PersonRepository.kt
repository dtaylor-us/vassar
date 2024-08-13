package org.vassar.api.adapter.out.persistence

import org.springframework.data.domain.Pageable
import org.springframework.data.neo4j.repository.ReactiveNeo4jRepository
import org.springframework.stereotype.Repository
import org.vassar.api.domain.Postnomial
import reactor.core.publisher.Flux
import reactor.core.publisher.Mono
import java.time.LocalDate

@Repository
interface PersonRepository : ReactiveNeo4jRepository<PersonNode, String> {
    fun findByFirstNameAndLastName(firstName: String, lastName: String): Mono<PersonNode>
    fun save(personNode: PersonNode): Mono<PersonNode>
    fun findByFirstNameAndLastNameAndBirthdate(firstName: String, lastName: String, birthdate: LocalDate): Mono<PersonNode>
    fun findByFirstNameAndLastNameAndPostnomial(firstName: String, lastName: String, postnomial: Postnomial): Mono<PersonNode>

}
