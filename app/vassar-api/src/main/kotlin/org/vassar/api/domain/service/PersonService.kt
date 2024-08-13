package org.vassar.api.domain.service


import org.springframework.stereotype.Service
import org.vassar.api.domain.Postnomial
import org.vassar.api.adapter.out.persistence.PersonNode
import org.vassar.api.port.out.PersonPort
import org.vassar.api.port.`in`.LoadPersonUseCase
import org.vassar.api.port.`in`.QueryPeopleUseCase
import reactor.core.publisher.Mono

// implements use case
@Service
class PersonService(private val personPort: PersonPort) : LoadPersonUseCase, QueryPeopleUseCase {

    override fun findByName(firstName: String, lastName: String, postnomial: Postnomial?): Mono<PersonNode> = personPort.findByName(firstName, lastName, postnomial)
    override fun getGenealogyTree(): Mono<List<PersonNode>> = personPort.getGenealogyTree()
    override fun loadPerson(person: PersonNode): Mono<PersonNode> = personPort.loadPerson(person)
}
