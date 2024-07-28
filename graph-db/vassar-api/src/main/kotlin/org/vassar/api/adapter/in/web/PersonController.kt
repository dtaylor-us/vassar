package org.vassar.api.adapter.`in`.web

import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import org.vassar.api.Postnomial
import org.vassar.api.adapter.out.persistence.PersonNode
import org.vassar.api.port.`in`.LoadPersonUseCase
import org.vassar.api.port.`in`.QueryPeopleUseCase
import reactor.core.publisher.Mono

@RestController
@RequestMapping("/people")
class PersonController(private val loadPersonUseCase: LoadPersonUseCase, private val queryPeopleUseCase: QueryPeopleUseCase) {

    @GetMapping
    fun findByPersonName(@RequestParam firstName: String, @RequestParam lastName: String, @RequestParam postnomial: Postnomial?): Mono<ResponseEntity<PersonNode>> =
        Mono.from(queryPeopleUseCase.findByName(firstName, lastName, postnomial))
            .map { ResponseEntity.ok(it) }
        .defaultIfEmpty(ResponseEntity.notFound().build())

    @PostMapping("/create")
    fun createPerson(@RequestBody person: PersonNode): Mono<ResponseEntity<PersonNode>> =
        Mono.from(loadPersonUseCase.loadPerson(person))
            .map { ResponseEntity.ok(it) }
            .defaultIfEmpty(ResponseEntity.notFound().build())
}
