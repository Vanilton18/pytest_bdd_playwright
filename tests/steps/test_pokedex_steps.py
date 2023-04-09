from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import parse

scenarios('../features/pokedex.feature')

@given('the pokédex page')
def the_pokedex_page(browser):
    browser.goto('/')


@when(parse('the user searches for "{texto}"'), converters=dict(texto=str))
def the_user_searches_for_text(browser, texto):
    search_input = browser.locator('#monsters-search-bar')
    search_input.fill(texto)


@then(parse('the "{pokemon}" information is shown'), converters=dict(pokemon=str))
def the_pokemon_information_is_shown(browser, pokemon):
    results = browser.locator('#monsters-list').all_inner_texts()

    assert results.__len__() > 0
    assert pokemon in results[0]