package org.vassar.api.adapter.out.persistence

data class Email(val value: String) {
    init {
        require(value.matches(Regex("^[A-Za-z0-9+_.-]+@(.+)$"))) { "Invalid email address" }
    }
}
