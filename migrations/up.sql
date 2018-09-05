
CREATE TABLE IF NOT EXISTS user_account(
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  last_login TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION update_last_login(id INT) RETURNS TIMESTAMP AS $$
#variable_conflict use_variable
DECLARE
  currtime TIMESTAMP := NOW();
BEGIN
  UPDATE user_account SET last_login = currtime WHERE user_account.id = id;
  RETURN currtime;
END;
$$ LANGUAGE plpgsql;

CREATE TABLE IF NOT EXISTS user_profile(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  address1 VARCHAR(255) NOT NULL,
  address2 VARCHAR(255),
  postal_code VARCHAR(12) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  profile_image VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  stripe_token VARCHAR(255) NOT NULL,
  date_created TIMESTAMP NOT NULL DEFAULT NOW(),
  user_account_id INTEGER REFERENCES user_account(id) ON DELETE CASCADE NOT NULL
);

CREATE OR REPLACE FUNCTION trigger_update_timestamp()
  RETURNS TRIGGER AS $$
BEGIN
  NEW.last_modified = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TABLE IF NOT EXISTS campaign(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  image VARCHAR(255) NOT NULL,
  amount_requested MONEY NOT NULL ,
  date_created TIMESTAMP NOT NULL DEFAULT NOW(),
  last_modified TIMESTAMP NOT NULL DEFAULT NOW()
);

DROP TRIGGER IF EXISTS update_timestamp ON campaign;
CREATE TRIGGER update_timestamp BEFORE UPDATE ON campaign FOR EACH ROW EXECUTE PROCEDURE trigger_update_timestamp();


DO $$ BEGIN
  CREATE TYPE roles AS ENUM('owner', 'watching', 'pledged');
  EXCEPTION
  WHEN duplicate_object THEN null;
END $$;


CREATE TABLE IF NOT EXISTS stripe_transaction(
  id SERIAL PRIMARY KEY,
  date_created TIMESTAMP NOT NULL DEFAULT NOW(),
  stripe_transaction_id VARCHAR(255) NOT NULL,
  amount MONEY NOT NULL
);

CREATE TABLE IF NOT EXISTS campaign_relation(
  id SERIAL PRIMARY KEY,
  user_account_id INTEGER REFERENCES user_account(id) ON DELETE CASCADE NOT NULL,
  campaign_id INTEGER REFERENCES campaign(id) ON DELETE CASCADE NOT NULL,
  transaction_id INTEGER REFERENCES stripe_transaction(id) ON DELETE CASCADE,
  user_role roles,
  CONSTRAINT if_pledged_then_transaction_must_exist CHECK(
    NOT (user_role = 'pledged' AND transaction_id IS NULL)
  )
);

