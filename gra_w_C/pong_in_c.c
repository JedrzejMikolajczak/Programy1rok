#define _CRT_SECURE_NO_WARNINGS
#include "raylib.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef enum {
    MENU,
    GAME,
    EXIT
} GameScreen;

bool DrawButton(Rectangle button, const char* text) {
    Vector2 mouse = GetMousePosition();
    bool hovered = CheckCollisionPointRec(mouse, button);
    bool clicked = hovered && IsMouseButtonPressed(MOUSE_LEFT_BUTTON);

    DrawRectangleRec(button, hovered ? LIGHTGRAY : GRAY);
    DrawRectangleLinesEx(button, 2, DARKGRAY);

    int textWidth = MeasureText(text, 20);
    DrawText(text, button.x + (button.width - textWidth) / 2, button.y + 10, 20, BLACK);

    return clicked;
}

int player_score = 0;
int player2_score = 0;
int bounces = 1;
int player1_ball = -1;
int if_point_get = 0;

void SaveScoreToFile() {
    FILE* file = fopen("save.txt", "w");
    if (file) {
        fprintf(file, "%d %d\n", player_score, player2_score);
        fclose(file);
    }
}

void LoadScoreFromFile() {
    FILE* file = fopen("save.txt", "r");
    if (file) {
        fscanf(file, "%d %d", &player_score, &player2_score);
        fclose(file);
    }
}

typedef struct {
    float x, y;
    float width, height;
    int speed;
} Player;

typedef struct {
    float x, y;
    float width, height;
    int speed;
} Player2;

typedef struct {
    float x, y;
    int speed_x, speed_y;
    int radius;
} Ball;

typedef struct {
    float x, y;
    float width, height;
    int speed_decrease;
    int is_visible;
    int is_taken;
} PowerUp_slow;

typedef struct {
    float x, y;
    float width, height;
    int size_decrease;
    int is_visible;
    int is_taken;
} PowerUp_palette_minimalize;

typedef struct {
    float x, y;
    float width, height;
    int is_visible;
    int is_taken;
} PowerUp_movement_reversed;

Ball ball;
Player player;
Player2 player2;
PowerUp_slow powerup_slow;
PowerUp_palette_minimalize powerup_palette_minimalize;
PowerUp_movement_reversed powerup_movement_reversed;

void BallReset() {
    ball.x = GetScreenWidth() / 2;
    ball.y = GetScreenHeight() / 2;
    int wybor_strony[] = { -1, 1 };
    ball.speed_x = 7 * wybor_strony[GetRandomValue(0, 1)];
    ball.speed_y = 7 * wybor_strony[GetRandomValue(0, 1)];
    bounces = 0;
}

void ResetGame() {
    BallReset();

    player.x = GetScreenWidth() - 35;
    player.y = GetScreenHeight() / 2 - 60;
    player.width = 25;
    player.height = 120;
    player.speed = 6;

    player2.x = 20;
    player2.y = GetScreenHeight() / 2 - 60;
    player2.width = 25;
    player2.height = 120;
    player2.speed = 6;

    powerup_slow.x = GetRandomValue(100, 1100);
    powerup_slow.y = GetRandomValue(100, 800);
    powerup_slow.width = 25;
    powerup_slow.height = 25;
    powerup_slow.speed_decrease = 1;
    powerup_slow.is_visible = 1;
    powerup_slow.is_taken = 0;

    powerup_palette_minimalize.x = GetRandomValue(100, 1100);
    powerup_palette_minimalize.y = GetRandomValue(100, 800);
    powerup_palette_minimalize.width = 25;
    powerup_palette_minimalize.height = 25;
    powerup_palette_minimalize.size_decrease = 30;
    powerup_palette_minimalize.is_visible = 1;
    powerup_palette_minimalize.is_taken = 0;

    powerup_movement_reversed.x = GetRandomValue(100, 1100);
    powerup_movement_reversed.y = GetRandomValue(100, 800);
    powerup_movement_reversed.width = 25;
    powerup_movement_reversed.height = 25;
    powerup_movement_reversed.is_visible = 1;
    powerup_movement_reversed.is_taken = 0;

    if_point_get = 0;
    player1_ball = -1;
}

int main() {
    srand(time(NULL));
    const int screenWidth = 1280;
    const int screenHeight = 800;

    InitWindow(screenWidth, screenHeight, "Pong Game z Menu");
    SetTargetFPS(60);

    GameScreen currentScreen = MENU;

    Rectangle playBtn = { screenWidth / 2 - 100, 300, 200, 50 };
    Rectangle loadBtn = { screenWidth / 2 - 100, 370, 200, 50 };
    Rectangle exitBtn = { screenWidth / 2 - 100, 440, 200, 50 };
    Rectangle saveBtn = { screenWidth - 150, 20, 120, 40 };

    ball.radius = 20;
    ball.x = screenWidth / 2;
    ball.y = screenHeight / 2;
    ball.speed_x = 7;
    ball.speed_y = 7;

    ResetGame();

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);

        if (currentScreen == MENU) {
            DrawText("MENU", screenWidth / 2 - MeasureText("MENU", 40) / 2, 200, 40, DARKBLUE);

            if (DrawButton(playBtn, "Play"))
                currentScreen = GAME;
            if (DrawButton(loadBtn, "Load Game")) {
                LoadScoreFromFile();
                currentScreen = GAME;
                ResetGame();
            }
            if (DrawButton(exitBtn, "Exit")) currentScreen = EXIT;
        }
        else if (currentScreen == GAME) {
            ClearBackground(BLACK);
            if (IsKeyPressed(KEY_ESCAPE)) {
                currentScreen = MENU;
                ResetGame();
            }

            Vector2 ballPos = { ball.x, ball.y };
            ball.x += ball.speed_x;
            ball.y += ball.speed_y;

            if (ball.y + ball.radius >= screenHeight || ball.y - ball.radius <= 0) ball.speed_y *= -1;
            if (ball.x + ball.radius >= screenWidth) {
                player_score++;
                if_point_get = 1;
                BallReset();
            }
            if (ball.x - ball.radius <= 0) {
                player2_score++;
                if_point_get = 1;
                BallReset();
            }

            if (IsKeyDown(KEY_UP)) player.y -= player.speed;
            if (IsKeyDown(KEY_DOWN)) player.y += player.speed;
            if (player.y <= 0) player.y = 0;
            if (player.y + player.height >= screenHeight) player.y = screenHeight - player.height;

            if (IsKeyDown(KEY_W)) player2.y -= player2.speed;
            if (IsKeyDown(KEY_S)) player2.y += player2.speed;
            if (player2.y <= 0) player2.y = 0;
            if (player2.y + player2.height >= screenHeight) player2.y = screenHeight - player2.height;

            Rectangle rect1 = { player.x, player.y, player.width, player.height };
            Rectangle rect2 = { player2.x, player2.y, player2.width, player2.height };

            if (CheckCollisionCircleRec(ballPos, ball.radius, rect1) && ball.speed_x > 0) {
                ball.speed_x *= -1;
                bounces++;
                player1_ball = 1;
                if (bounces % 6 == 0) {
                    if (ball.speed_x > 0) {
                        ball.speed_x += 1;
                    }
                    else {
                        ball.speed_x -= 1;
                    }

                    if (ball.speed_y > 0) {
                        ball.speed_y += 1;
                    }
                    else {
                        ball.speed_y -= 1;
                    }
                }
            }

            if (CheckCollisionCircleRec(ballPos, ball.radius, rect2) && ball.speed_x < 0) {
                ball.speed_x *= -1;
                bounces++;
                player1_ball = 1;
                if (bounces % 6 == 0) {
                    if (ball.speed_x > 0) {
                        ball.speed_x += 1;
                    }
                    else {
                        ball.speed_x -= 1;
                    }

                    if (ball.speed_y > 0) {
                        ball.speed_y += 1;
                    }
                    else {
                        ball.speed_y -= 1;
                    }
                }
            }

            Rectangle slowRect = { powerup_slow.x, powerup_slow.y, powerup_slow.width, powerup_slow.height };
            Rectangle minRect = { powerup_palette_minimalize.x, powerup_palette_minimalize.y, powerup_palette_minimalize.width, powerup_palette_minimalize.height };
            Rectangle revRect = { powerup_movement_reversed.x, powerup_movement_reversed.y, powerup_movement_reversed.width, powerup_movement_reversed.height };

            if (CheckCollisionCircleRec(ballPos, ball.radius, slowRect) && powerup_slow.is_visible && !powerup_slow.is_taken) {
                powerup_slow.is_visible = 0;
                if (player1_ball == 1) player2.speed -= powerup_slow.speed_decrease;
                else if (player1_ball == 0) player.speed -= powerup_slow.speed_decrease;
                powerup_slow.is_taken = 1;
            }

            if (CheckCollisionCircleRec(ballPos, ball.radius, minRect) && powerup_palette_minimalize.is_visible && !powerup_palette_minimalize.is_taken) {
                powerup_palette_minimalize.is_visible = 0;
                if (player1_ball == 1) player2.height -= powerup_palette_minimalize.size_decrease;
                else if (player1_ball == 0) player.height -= powerup_palette_minimalize.size_decrease;
                powerup_palette_minimalize.is_taken = 1;
            }

            if (CheckCollisionCircleRec(ballPos, ball.radius, revRect) && powerup_movement_reversed.is_visible && !powerup_movement_reversed.is_taken) {
                powerup_movement_reversed.is_visible = 0;
                if (player1_ball == 1) player2.speed *= -1;
                else if (player1_ball == 0) player.speed *= -1;
                powerup_movement_reversed.is_taken = 1;
            }

            if (if_point_get) ResetGame();

            DrawLine(screenWidth / 2, 0, screenWidth / 2, screenHeight, WHITE);
            DrawCircle(ball.x, ball.y, ball.radius, WHITE);
            DrawRectangle(player.x, player.y, player.width, player.height, WHITE);
            DrawRectangle(player2.x, player2.y, player2.width, player2.height, WHITE);

            if (powerup_slow.is_visible && player1_ball >= 0) DrawRectangle(powerup_slow.x, powerup_slow.y, powerup_slow.width, powerup_slow.height, RED);
            if (powerup_palette_minimalize.is_visible && player1_ball >= 0) DrawRectangle(powerup_palette_minimalize.x, powerup_palette_minimalize.y, powerup_palette_minimalize.width, powerup_palette_minimalize.height, GREEN);
            if (powerup_movement_reversed.is_visible && player1_ball >= 0) DrawRectangle(powerup_movement_reversed.x, powerup_movement_reversed.y, powerup_movement_reversed.width, powerup_movement_reversed.height, BLUE);

            DrawText(TextFormat("%i", player_score), screenWidth / 4 - 20, 20, 80, WHITE);
            DrawText(TextFormat("%i", player2_score), 3 * screenWidth / 4 - 20, 20, 80, WHITE);

            if (DrawButton(saveBtn, "Save&Exit")) {
                SaveScoreToFile();
                CloseWindow();
                return 0;
            }
        }
        else if (currentScreen == EXIT) {
            CloseWindow();
            return 0;
        }
        EndDrawing();
    }

    CloseWindow();
    return 0;
}

