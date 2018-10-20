ALTER TABLE user_account ADD COLUMN first_name VARCHAR(255) NOT NULL;
ALTER TABLE user_account ADD COLUMN last_name VARCHAR(255) NOT NULL;
ALTER TABLE user_account ADD COLUMN address1 VARCHAR(255) NOT NULL;
ALTER TABLE user_account ADD COLUMN address2 VARCHAR(255);
ALTER TABLE user_account ADD COLUMN postal_code VARCHAR(12) NOT NULL;
ALTER TABLE user_account ADD COLUMN phone_number VARCHAR(20) NOT NULL;
ALTER TABLE user_account ADD COLUMN profile_image VARCHAR(255) NOT NULL;
ALTER TABLE user_account ADD COLUMN description TEXT NOT NULL;
ALTER TABLE user_account ADD COLUMN credit_card VARCHAR(16);
ALTER TABLE user_account ADD COLUMN tsv tsvector;

DROP TABLE user_profile;

ALTER TABLE user_account DROP CONSTRAINT user_account_pkey CASCADE;
ALTER TABLE user_account DROP COLUMN id;
ALTER TABLE user_account DROP CONSTRAINT user_account_email_key;
ALTER TABLE user_account ADD CONSTRAINT user_account_pkey PRIMARY KEY (email);

ALTER TABLE campaign_relation DROP COLUMN user_account_id;
ALTER TABLE campaign_relation ADD COLUMN user_account_email VARCHAR(255) REFERENCES user_account(email) ON DELETE CASCADE NOT NULL;