package org.vassar.api.domain.service


import org.springframework.stereotype.Service
import org.vassar.api.Postnomial
import org.vassar.api.adapter.out.persistence.PersonNode
import org.vassar.api.port.out.PersonPort
import org.vassar.api.port.`in`.LoadPersonUseCase
import org.vassar.api.port.`in`.QueryPeopleUseCase
import reactor.core.publisher.Mono

// implements use case
@Service
class PersonService(private val personPort: PersonPort) : LoadPersonUseCase, QueryPeopleUseCase {

    override fun findByName(firstName: String, lastName: String, postnomial: Postnomial?): Mono<PersonNode> {
        return personPort.findByName(firstName, lastName, postnomial)
    }

    override fun listAll(page: Int, size: Int): Mono<List<PersonNode>> {
        return personPort.listAll(page, size)
    }

    override fun loadPerson(person: PersonNode): Mono<PersonNode> {
        return personPort.loadPerson(person)
    }
}
