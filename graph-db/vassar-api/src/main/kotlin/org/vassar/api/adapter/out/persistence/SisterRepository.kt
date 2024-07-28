package org.vassar.api.adapter.out.persistence

import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository

@Repository
interface SisterRepository : CrudRepository<PersonNode, String> {
}
