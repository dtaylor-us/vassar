package org.vassar.api

import org.springframework.boot.CommandLineRunner
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.vassar.api.adapter.out.persistence.Email
import org.vassar.api.adapter.out.persistence.Gender
import org.vassar.api.adapter.out.persistence.PersonNode
import org.vassar.api.adapter.out.persistence.PersonPersistenceAdapter
import java.time.LocalDate

@Configuration
class DataInitializer {
    @Bean
    fun init(userRepository: PersonPersistenceAdapter): CommandLineRunner {
        return CommandLineRunner {
            val benjaminHarrisonIV = PersonNode(
                firstName = "Benjamin",
                lastName = "Harrison",
                postnomial = Postnomial.IV,
                birthdate = LocalDate.parse("1693-09-11"),
                deathOfDate = LocalDate.parse("1745-07-12"),
                email = Email("benjamin.harrison.iv@email.com"),
                gender = Gender.MALE,
                occupation = listOf("Lawyer", "Burgess and High Sheriff", "Member of Virginia House of Burgesses"),
                bio = "Benjamin Harrison IV was an American Virginia planter, politician, and member of the Virginia House of Burgesses.",
                children = listOf(),
                parents = listOf()
            )

            val benjaminHarrisonV = PersonNode(
                firstName = "Benjamin",
                lastName = "Harrison",
                postnomial = Postnomial.V,
                birthdate = LocalDate.parse("1726-04-05"),
                deathOfDate = LocalDate.parse("1791-04-24"),
                email = Email("benjamin.harrison.v@email.com"),
                gender = Gender.MALE,
                occupation = listOf("Member of the Virginia House of Burgesses", "Signer of the Declaration of Independence"),
                bio = "Benjamin Harrison V was an American planter and merchant, a revolutionary leader, and a Founding Father of the United States.",
                children = listOf(),
                parents = listOf()
            )

            val elizabethBassett = PersonNode(
                firstName = "Elizabeth",
                lastName = "Bassett",
                postnomial = Postnomial.NONE,
                birthdate = LocalDate.parse("1730-01-01"),
                deathOfDate = LocalDate.parse("1792-02-13"),
                email = Email("elizabeth.bassett@email.com"),
                gender = Gender.FEMALE,
                occupation = listOf(),
                bio = "Elizabeth Bassett Harrison was the wife of Benjamin Harrison V and the mother of William Henry Harrison, the ninth President of the United States.",
                children = listOf(),
                parents = listOf()
            )

            // Setting relationships
            benjaminHarrisonIV.children = listOf(benjaminHarrisonV)
            benjaminHarrisonV.parents = listOf(benjaminHarrisonIV)
            benjaminHarrisonV.children = listOf()
            elizabethBassett.children = listOf()

            // Add spouse relationship
            benjaminHarrisonV.spouse = elizabethBassett
            elizabethBassett.spouse = benjaminHarrisonV

            // Saving people and relationships to the repository
            userRepository.loadPerson(benjaminHarrisonIV).subscribe()
            userRepository.loadPerson(benjaminHarrisonV).subscribe()
            userRepository.loadPerson(elizabethBassett).subscribe()
        }
    }
}
