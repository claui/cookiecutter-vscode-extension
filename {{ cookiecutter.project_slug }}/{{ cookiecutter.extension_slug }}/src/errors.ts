export default class ValueError extends Error {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options);
  }
}
