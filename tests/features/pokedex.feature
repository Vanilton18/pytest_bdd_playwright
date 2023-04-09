Feature: pokédex search
  As a Pokemon trainer,
  I want to search for pokemons in my pokédex,
  So I can learn more about them.

  Background:
    Given the pokédex page

  Scenario Outline: Name pokédex search
    When the user searches for "<text>"
    Then the "<pokemon>" information is shown

    Examples: Pokemons
      | text       | pokemon    |
      | Pikachu    | Pikachu    |
      | Charmander | Charmander |

  @tag1
  Scenario Outline: Name pokédex search2
    When the user searches for "<text>"
    Then the "<pokemon>" information is shown

    Examples: Pokemons
      | text       | pokemon    |
      | Pikachu    | Pikachu    |
      | Charmander | Charmander |