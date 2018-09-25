DO $$ BEGIN
  CREATE TYPE status AS ENUM('super', 'default', 'suspended');
  EXCEPTION
  WHEN duplicate_object THEN null;
END $$;

ALTER TABLE user_account ADD COLUMN account_status status ;
ALTER TABLE campaign ADD COLUMN campaign_status status ;

-- Pass is cs2102pass and there is no profile for admin
INSERT INTO user_account (email, password, last_login, date_created, account_status)
VALUES ('admin@onus.com', 'pbkdf2:sha256:50000$uISlYTwd$9885eac29aa343d3776d1e2923234becdbe23c142589969f08ffa5beb05139bc', now(), now(), 'super');
