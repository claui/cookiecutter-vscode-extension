export default interface Logger {
  debug(...args: unknown[]): void;
  error(...args: unknown[]): void;
  info(...args: unknown[]): void;
  log(level: string, ...args: unknown[]): void;
}
