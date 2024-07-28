package org.vassar.api

import org.junit.jupiter.api.Test
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.data.neo4j.repository.config.EnableReactiveNeo4jRepositories
import org.springframework.transaction.annotation.EnableTransactionManagement

@SpringBootTest
class VassarApiApplicationTests {

    @Test
    fun contextLoads() {
    }

}
