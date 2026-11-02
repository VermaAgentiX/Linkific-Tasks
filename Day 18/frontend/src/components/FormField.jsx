export default function FormField({ name, label, value, error, onChange, ...inputProps }) {
  return (
    <label className="form-field">
      {label}
      <input
        name={name}
        value={value}
        onChange={onChange}
        aria-invalid={Boolean(error)}
        aria-describedby={error ? `${name}-error` : undefined}
        {...inputProps}
      />
      {error && (
        <small className="field-error" id={`${name}-error`} role="alert">
          {error}
        </small>
      )}
    </label>
  );
}
