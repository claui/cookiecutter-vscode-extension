import { hello } from "{{ cookiecutter.extension_slug }}";

describe("the hello function", () => {
  it("returns a default value", () => {
    expect(hello())
      .toBe("Hello, world!");
  });

  it("greets the author", () => {
    expect(hello("{{ cookiecutter.author_full_name }}"))
      .toBe("Hello, {{ cookiecutter.author_full_name }}!")
  });
});
