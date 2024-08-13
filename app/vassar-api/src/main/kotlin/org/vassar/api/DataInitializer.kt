package org.vassar.api

import org.springframework.boot.CommandLineRunner
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.vassar.api.domain.Email
import org.vassar.api.domain.Gender
import org.vassar.api.adapter.out.persistence.PersonNode
import org.vassar.api.adapter.out.persistence.PersonPersistenceAdapter
import org.vassar.api.domain.Postnomial
import java.time.LocalDate

@Configuration
class DataInitializer {
    @Bean
    fun init(userRepository: PersonPersistenceAdapter): CommandLineRunner {
        userRepository.deleteAll().block()
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

            val williamHenryHarrison = PersonNode(
                firstName = "William Henry",
                lastName = "Harrison",
                postnomial = Postnomial.NONE,
                birthdate = LocalDate.parse("1773-02-09"),
                deathOfDate = LocalDate.parse("1841-04-04"),
                email = Email("william.henry.harrison@email.com"),
                gender = Gender.MALE,
                occupation = listOf("9th President of the United States"),
                bio = "William Henry Harrison was an American military officer and politician who served as the ninth president of the United States.",
                children = listOf(),
                parents = listOf()
            )

            val dilsia = PersonNode(
                firstName = "Dilsia",
                lastName = "Unknown",
                postnomial = Postnomial.NONE,
                birthdate = LocalDate.parse("1800-01-01"), // approximate date
                deathOfDate = LocalDate.parse("1850-01-01"), // approximate date
                email = Email("dilsia@email.com"),
                gender = Gender.FEMALE,
                occupation = listOf("Slave"),
                bio = "Dilsia was a slave who had a son, Oliver, with William Henry Harrison.",
                children = listOf(),
                parents = listOf()
            )

            val oliverHarrison = PersonNode(
                firstName = "Oliver",
                lastName = "Harrison",
                postnomial = Postnomial.NONE,
                birthdate = LocalDate.parse("1816-01-01"),
                deathOfDate = LocalDate.parse("1900-01-01"), // approximate date
                email = Email("oliver.harrison@email.com"),
                gender = Gender.MALE,
                occupation = listOf(),
                bio = "Oliver Harrison was the son of Dilsia and William Henry Harrison.",
                children = listOf(),
                parents = listOf()
            )

            val margaretWills = PersonNode(
                firstName = "Margaret",
                lastName = "Wills",
                postnomial = Postnomial.NONE,
                birthdate = LocalDate.parse("1818-01-01"), // approximate date
                deathOfDate = LocalDate.parse("1890-01-01"), // approximate date
                email = Email("margaret.wills@email.com"),
                gender = Gender.FEMALE,
                occupation = listOf(),
                bio = "Margaret Wills was the spouse of Oliver Harrison and the mother of Mary Ann Harrison.",
                children = listOf(),
                parents = listOf()
            )

            val maryAnnHarrison = PersonNode(
                firstName = "Mary Ann",
                lastName = "Harrison",
                postnomial = Postnomial.NONE,
                birthdate = LocalDate.parse("1838-01-01"), // approximate date
                deathOfDate = LocalDate.parse("1910-01-01"), // approximate date
                email = Email("mary.ann.harrison@email.com"),
                gender = Gender.FEMALE,
                occupation = listOf(),
                bio = "Mary Ann Harrison was the daughter of Oliver Harrison and Margaret Wills.",
                children = listOf(),
                parents = listOf()
            )

            // Setting relationships
            benjaminHarrisonIV.children = listOf(benjaminHarrisonV)
            benjaminHarrisonV.parents = listOf(benjaminHarrisonIV)
            benjaminHarrisonV.children = listOf(williamHenryHarrison)
            elizabethBassett.children = listOf()

            // Add spouse relationship
            benjaminHarrisonV.spouse = elizabethBassett
            elizabethBassett.spouse = benjaminHarrisonV

            // Add parent-child relationships for William Henry Harrison
            williamHenryHarrison.children = listOf(oliverHarrison)
            oliverHarrison.parents = listOf(williamHenryHarrison, dilsia)
            dilsia.children = listOf(oliverHarrison)

            // Add parent-child relationships for Oliver Harrison
            oliverHarrison.children = listOf(maryAnnHarrison)
            maryAnnHarrison.parents = listOf(oliverHarrison, margaretWills)
            margaretWills.children = listOf(maryAnnHarrison)

            // Saving people and relationships to the repository
            userRepository.loadPerson(benjaminHarrisonIV).subscribe()
            userRepository.loadPerson(benjaminHarrisonV).subscribe()
            userRepository.loadPerson(elizabethBassett).subscribe()
            userRepository.loadPerson(williamHenryHarrison).subscribe()
            userRepository.loadPerson(dilsia).subscribe()
            userRepository.loadPerson(oliverHarrison).subscribe()
            userRepository.loadPerson(margaretWills).subscribe()
            userRepository.loadPerson(maryAnnHarrison).subscribe()
        }
    }

}
