Given("I am on the home page") do
  visit root_path
end

Given("I am on the allRecipes page") do
  visit allRecipes_path
end

Given("I am on the basket page") do
  visit basket_path
end

When("I click on the {string} link") do |page_name|
  click_link page_name
end

Then("I should be on the {string} page") do |page_name|
  expect(page).to have_content(page_name)
end

