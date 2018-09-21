ALTER TABLE campaign ADD COLUMN tsv tsvector;
ALTER TABLE user_profile ADD COLUMN tsv tsvector;

DROP TRIGGER IF EXISTS tsv_update_campaign ON campaign;
CREATE TRIGGER tsv_update_campaign BEFORE INSERT OR UPDATE
  ON campaign FOR EACH ROW EXECUTE PROCEDURE
  tsvector_update_trigger(tsv, 'pg_catalog.english', name, description);

DROP TRIGGER IF EXISTS tsv_update_user_profile ON user_profile;
CREATE TRIGGER tsv_update_user_profile BEFORE INSERT OR UPDATE
  ON user_profile FOR EACH ROW EXECUTE PROCEDURE
  tsvector_update_trigger(tsv, 'pg_catalog.english', first_name, last_name, description);
