BEGIN TRANSACTION;

INSERT INTO Commodity VALUES ('0001', 'Tshirt' ,'clothes', 1000, 500, '2009-09-20');
INSERT INTO Commodity VALUES ('0002', 'hole_puncher', 'office_supplies', 500, 320, '2009-09-11');
INSERT INTO Commodity VALUES ('0003', 'sport_Tshirt', 'clothes', 4000, 2800, NULL);
INSERT INTO Commodity VALUES ('0004', 'knife', 'kitchenware', 3000, 2800, '2009-09-20');
INSERT INTO Commodity VALUES ('0005', 'pressure_cooker', 'kitchenware', 6800, 5000, '2009-01-15');
INSERT INTO Commodity VALUES ('0006', 'fork', 'kitchenware', 500, NULL, '2009-09-20');
INSERT INTO Commodity VALUES ('0007', 'grater', 'kitchenware', 880, 790, '2008-04-28');
INSERT INTO Commodity VALUES ('0008', 'ball_point_pen', 'office_supplies', 100, NULL, '2009-11-11');

COMMIT;
