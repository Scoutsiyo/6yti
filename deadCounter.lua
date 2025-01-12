-- Este script debe colocarse en un LocalScript dentro de StarterPlayerScripts


-- Crear una pantalla GUI para el contador de muertes
local player = game.Players.LocalPlayer

local screenGui = Instance.new("ScreenGui")
screenGui.Name = "DeathCounterGui"
screenGui.Parent = player:WaitForChild("PlayerGui")


local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 200, 0, 50)
frame.Position = UDim2.new(0, 10, 0, 10) -- Esquina superior izquierda
frame.BackgroundTransparency = 0.5
frame.BackgroundColor3 = Color3.new(0, 0, 0) -- Fondo negro semitransparente
frame.Parent = screenGui


local textLabel = Instance.new("TextLabel")
textLabel.Size = UDim2.new(1, 0, 1, 0)
textLabel.BackgroundTransparency = 1
textLabel.TextColor3 = Color3.new(1, 1, 1) -- Texto blanco
textLabel.TextScaled = true
textLabel.Font = Enum.Font.SourceSansBold
textLabel.Text = "Muertes: 0"
textLabel.Parent = frame


local function updateDeathCount()
    local leaderstats = player:FindFirstChild("leaderstats")
    if leaderstats then
        local deaths = leaderstats:FindFirstChild("Deaths")
        if deaths then
            textLabel.Text = "Muertes: " .. tostring(deaths.Value)
        end
    end
end


player:WaitForChild("leaderstats"):WaitForChild("Deaths").Changed:Connect(updateDeathCount)


updateDeathCount()
