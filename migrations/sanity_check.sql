-- TODO : migrate all of these into a test suite

-- Does everything insert nicely?
INSERT INTO user_account (email, password, salt, last_login, date_created)
VALUES ('test@test.com', 'fakehash', 'salt', now(), now());

INSERT INTO user_profile (first_name, last_name, address1, address2, postal_code, phone_number, profile_image, description, stripe_token, date_created, user_account_id)
VALUES ('First', 'Last', 'Address Line 1', NULL, '654456', '+123321123', '\test.jpg', 'Looking 4 Luv Lmao', 'stripe_token', now(), 1);

INSERT INTO campaign(name, description, image, amount_requested)
VALUES ('Make America Great Again', 'Buy me a metric ton of MAGA hats and launch it into space!', '\url\to\image.jpg', 9999.999);

INSERT INTO campaign_relation(user_account_id, campaign_id, user_role)
VALUES (1, 1, 'owner');

INSERT INTO stripe_transaction(stripe_transaction_id, amount)
VALUES ('stripe_transacation_ id', 999.00);

INSERT INTO stripe_transaction(stripe_transaction_id, amount)
VALUES ('stripe_transacation_ id', 10000.00);

INSERT INTO campaign_relation(user_account_id, campaign_id, transaction_id, user_role)
VALUES (1, 1, 1, 'pledged');

INSERT INTO campaign_relation(user_account_id, campaign_id, transaction_id, user_role)
VALUES (1, 1, 2, 'pledged');

SELECT SUM(amount)
FROM campaign c INNER JOIN campaign_relation cr ON c.id = cr.campaign_id
INNER JOIN transaction t ON t.id = cr.transaction_id WHERE user_role='pledged' AND c.id=1;


-- Does everything below this fail as expected?

/*
-- Check that these violate our constrains (this is possibly happen if our hashing algo fails somehow)
INSERT INTO user_account (email, password, last_login, date_created) VALUES ('fail@test.com', NULL, now(), now());

-- Check that these violate our constrains (this is possibly happen if server side validation fails somehow)
INSERT INTO user_profile (first_name, last_name, address1, address2, postal_code, phone_number, profile_image, description, date_created, user_account_id)
VALUES (NULL, 'Last', 'Address Line 1', NULL, '654456', '+123321123', '\test.jpg', 'Looking 4 Luv Lmao', now(), 1);

-- Remove the user_account
DELETE FROM  user_account WHERE id=1;

-- Check that its user_profile is removed as well
SELECT * FROM user_account INNER JOIN user_profile u on user_account.id = u.user_account_id;

-- Check that campaign is inserted properly and timestamps are all set.
SELECT * FROM campaign;

-- Modify a row to trigger the function
UPDATE campaign SET amount_requested=10000.00 WHERE id=1;

-- Check that last_modified > date_created
SELECT * FROM campaign;

-- Check that it violates our conditional constraint
INSERT INTO campaign_relation(user_account_id, campaign_id, transaction_id, user_role)
VALUES (1, 1, null, 'pledged');
*/
