ALTER TABLE user_profile DROP COLUMN stripe_token;
ALTER TABLE user_profile ADD COLUMN credit_card VARCHAR(16);
ALTER TABLE stripe_transaction RENAME TO transaction;
ALTER TABLE transaction DROP COLUMN stripe_transaction_id;
ALTER TABLE transaction DROP CONSTRAINT stripe_transaction_pkey CASCADE;
ALTER TABLE transaction DROP COLUMN id;
ALTER TABLE transaction ADD COLUMN id SERIAL;
ALTER TABLE transaction ADD COLUMN credit_card VARCHAR(16);