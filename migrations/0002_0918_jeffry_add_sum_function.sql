CREATE OR REPLACE FUNCTION get_total_donations(id INT) RETURNS MONEY AS $$
#variable_conflict use_variable
DECLARE
  total MONEY;
BEGIN
  total := (SELECT SUM(amount)
            FROM campaign c INNER JOIN campaign_relation cr ON c.id = cr.campaign_id
            INNER JOIN transaction t ON t.id = cr.transaction_id WHERE user_role='pledged' and c.id=id);
  RETURN coalesce(total, '$0.00');
END;
$$ LANGUAGE plpgsql;