ALTER TABLE transaction ADD CONSTRAINT transaction_pkey PRIMARY KEY (id);
ALTER TABLE campaign_relation ADD CONSTRAINT campaign_relation_transaction_id_fkey
FOREIGN KEY (transaction_id) REFERENCES transaction(id);
ALTER TABLE transaction ALTER COLUMN credit_card SET NOT NULL;

CREATE OR REPLACE FUNCTION check_if_owner()
       RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS(SELECT cr.campaign_id, cr.user_account_email, cr.user_role
         FROM campaign_relation cr
         WHERE cr.campaign_id=NEW.campaign_id AND cr.user_account_email=NEW.user_account_email
         AND cr.user_role='owner')
  THEN
    DELETE FROM transaction
        WHERE id = NEW.transaction_id;
    RETURN NULL;
  ELSE
    RETURN NEW;
  end if;
end;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER check_if_owner_campaign_relation BEFORE INSERT OR UPDATE
       ON campaign_relation FOR EACH ROW
       WHEN (NEW.user_role='pledged')
       EXECUTE PROCEDURE check_if_owner();
