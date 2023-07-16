import ValueError from "./errors";

export function hello(name: string = "world") {
  if (!name) {
    throw new ValueError("Name cannot be empty.")
  }
  return `Hello, ${name}!`;
}
