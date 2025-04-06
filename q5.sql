SELECT 
    pg.Valor AS Salario,
    c.Nome AS Nome_Contratado,
    c.CPF
FROM 
    Contratado c
JOIN 
    Profissao p ON c.ID_Profissao = p.ID
JOIN 
    Pagamento pg ON c.ID = pg.ID_Contratado
WHERE 
    p.Nome_Profissao IN ('Advogado', 'Empresário');
