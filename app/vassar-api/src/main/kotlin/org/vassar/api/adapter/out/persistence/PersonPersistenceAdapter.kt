package org.vassar.api.adapter.out.persistence

import org.springframework.data.domain.PageRequest
import org.springframework.stereotype.Component
import org.vassar.api.domain.Postnomial
import org.vassar.api.port.out.PersonPort
import reactor.core.publisher.Mono

@Component
class PersonPersistenceAdapter(private val personRepository: PersonRepository) : PersonPort {
    override fun loadPerson(person: PersonNode): Mono<PersonNode> {
        return savePerson(person)
    }

    override fun findByName(firstName: String, lastName: String, postnomial: Postnomial?): Mono<PersonNode> {
        return when (postnomial) {
            null, Postnomial.NONE -> personRepository.findByFirstNameAndLastName(firstName, lastName).map { it }
            else -> personRepository.findByFirstNameAndLastNameAndPostnomial(firstName, lastName, postnomial)
        }
    }

//    override fun listAll(page: Int, size: Int): Mono<List<PersonNode>> {
//        val pageable = PageRequest.of(page, size)
//        return personRepository.findAll(pageable).collectList()
//    }

    override fun getGenealogyTree(): Mono<List<PersonNode>> {
        TODO("Not yet implemented")
    }

    override fun deleteAll(): Mono<Void> {
        return personRepository.deleteAll()
    }

    fun savePerson(person: PersonNode): Mono<PersonNode> {
        return personRepository.findByFirstNameAndLastNameAndBirthdate(
            person.firstName, person.lastName, person.birthdate
        ).flatMap { existingPerson ->
            if (existingPerson != null) {
                Mono.error(IllegalArgumentException("A person with the same first name, last name, and birthdate already exists."))
            } else {
                personRepository.save(person).map { it }
            }
        }
    }
}
