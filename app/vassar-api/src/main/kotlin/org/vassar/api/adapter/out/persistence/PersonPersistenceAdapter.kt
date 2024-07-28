package org.vassar.api.adapter.out.persistence

import org.springframework.stereotype.Component
import org.vassar.api.Postnomial
import org.vassar.api.port.PersonPort
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
